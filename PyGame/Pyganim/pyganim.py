# Pyganim (pyganim.py, ver 1)
# A sprite animation module for Pygame.
#
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pyganim
# Released under a "Simplified BSD" license
#
# There's a tutorial (and sample code) on how to use this library at http://inventwithpython.com/pyganim
# NOTE: This module requires Pygame to be installed to use. Download it from http://pygame.org
#
# This should be compatible with both Python 2 and Python 3. Please email any
# bug reports to Al at al@inventwithpython.com
#


# TODO: Feature idea: if the same image file is specified, re-use the Surface object. (Make this optional though.)

import pygame, time

# setting up constants
PLAYING = 'playing'
PAUSED = 'paused'
STOPPED = 'stopped'

# These values are used in the anchor() method.
NORTHWEST = 'northwest'
NORTH = 'north'
NORTHEAST = 'northeast'
WEST = 'west'
CENTER = 'center'
EAST = 'east'
SOUTHWEST = 'southwest'
SOUTH = 'south'
SOUTHEAST = 'southeast'


class PygAnimation(object):
    def __init__(self, frames, loop=True):
        # Constructor function for the animation object. Starts off in the STOPPED state.
        #
        # @param frames
        #     A list of tuples for each frame of animation, in one of the following format:
        #       (image_of_frame<pygame.Surface>, duration_in_seconds<int>)
        #       (filename_of_image<str>, duration_in_seconds<int>)
        #     Note that the images and duration cannot be changed. A new PygAnimation object
        #     will have to be created.
        # @param loop Tells the animation object to keep playing in a loop.

        # _images stores the pygame.Surface objects of each frame
        self._images = []
        # _durations stores the durations (in seconds) of each frame.
        # e.g. [1, 1, 2.5] means the first and second frames last one second,
        # and the third frame lasts for two and half seconds.
        self._durations = []
        # _startTimes shows when each frame begins. len(self._startTimes) will
        # always be one more than len(self._images), because the last number
        # will be when the last frame ends, rather than when it starts.
        # The values are in seconds.
        # So self._startTimes[-1] tells you the length of the entire animation.
        # e.g. if _durations is [1, 1, 2.5], then _startTimes will be [0, 1, 2, 4.5]
        self._startTimes = None

        # if the sprites are transformed, the originals are kept in _images
        # and the transformed sprites are kept in _transformedImages.
        self._transformedImages = []

        self._state = STOPPED # The state is always either PLAYING, PAUSED, or STOPPED
        self._loop = loop # If True, the animation will keep looping. If False, the animation stops after playing once.
        self._rate = 1.0 # 2.0 means play the animation twice as fast, 0.5 means twice as slow
        self._visibility = True # If False, then nothing is drawn when the blit() methods are called

        self._playingStartTime = 0 # the time that the play() function was last called.
        self._pausedStartTime = 0 # the time that the pause() function was last called.

        if frames != '_copy': # ('_copy' is passed for frames by the getCopies() method)
            self.numFrames = len(frames)
            assert self.numFrames > 0, 'Must contain at least one frame.'
            for i in range(self.numFrames):
                # load each frame of animation into _images
                frame = frames[i]
                assert type(frame) in (list, tuple) and len(frame) == 2, 'Frame %s has incorrect format.' % (i)
                assert type(frame[0]) in (str, pygame.Surface), 'Frame %s image must be a string filename or a pygame.Surface' % (i)
                assert frame[1] > 0, 'Frame %s duration must be greater than zero.' % (i)
                if type(frame[0]) == str:
                    frame = (pygame.image.load(frame[0]), frame[1])
                self._images.append(frame[0])
                self._durations.append(frame[1])
            self._startTimes = self._getStartTimes()


    def _getStartTimes(self):
        # Internal method to get the start times based off of the _durations list.
        # Don't call this method.
        startTimes = [0]
        for i in range(self.numFrames):
            startTimes.append(startTimes[-1] + self._durations[i])
        return startTimes


    def reverse(self):
        # Reverses the order of the animations.
        self.elapsed = self._startTimes[-1] - self.elapsed
        self._images.reverse()
        self._transformedImages.reverse()
        self._durations.reverse()


    def getCopy(self):
        # Returns a copy of this PygAnimation object, but one that refers to the
        # Surface objects of the original so it efficiently uses memory.
        #
        # NOTE: Messing around with the original Surface objects will affect all
        # the copies. If you want to modify the Surface objects, then just make
        # copies using constructor function instead.
        return self.getCopies(1)[0]


    def getCopies(self, numCopies=1):
        # Returns a list of copies of this PygAnimation object, but one that refers to the
        # Surface objects of the original so it efficiently uses memory.
        #
        # NOTE: Messing around with the original Surface objects will affect all
        # the copies. If you want to modify the Surface objects, then just make
        # copies using constructor function instead.
        retval = []
        for i in range(numCopies):
            newAnim = PygAnimation('_copy', loop=self.loop)
            newAnim._images = self._images[:]
            newAnim._transformedImages = self._transformedImages[:]
            newAnim._durations = self._durations[:]
            newAnim._startTimes = self._startTimes[:]
            newAnim.numFrames = self.numFrames
            retval.append(newAnim)
        return retval


    def blit(self, destSurface, dest):
        # Draws the appropriate frame of the animation to the destination Surface
        # at the specified position.
        #
        # NOTE: If the visibility attribute is False, then nothing will be drawn.
        #
        # @param destSurface
        #     The Surface object to draw the frame
        # @param dest
        #     The position to draw the frame. This is passed to Pygame's Surface's
        #     blit() function, so it can be either a (top, left) tuple or a Rect
        #     object.
        if self.isFinished():
            self.state = STOPPED
        if not self.visibility or self.state == STOPPED:
            return
        frameNum = findStartTime(self._startTimes, self.elapsed)
        destSurface.blit(self.getFrame(frameNum), dest)


    def getFrame(self, frameNum):
        # Returns the pygame.Surface object of the frameNum-th frame in this
        # animation object. If there is a transformed version of the frame,
        # it will return that one.
        if self._transformedImages == []:
            return self._images[frameNum]
        else:
            return self._transformedImages[frameNum]


    def getCurrentFrame(self):
        # Returns the pygame.Surface object of the frame that would be drawn
        # if the blit() method were called right now. If there is a transformed
        # version of the frame, it will return that one.
        return self.getFrame(self.currentFrameNum)


    def clearTransforms(self):
        # Deletes all the transformed frames so that the animation object
        # displays the original Surfaces/images as they were before
        # transformation functions were called on them.
        #
        # This is handy to do for multiple transformation, where calling
        # the rotation or scaling functions multiple times results in
        # degraded/noisy images.
        self._transformedImages = []

    def makeTransformsPermanent(self):
        self._images = [pygame.Surface(surfObj.get_size(), 0, surfObj) for surfObj in self._transformedImages]
        for i in range(len(self._transformedImages)):
            self._images[i].blit(self._transformedImages[i], (0,0))

    def blitFrameNum(self, frameNum, destSurface, dest):
        # Draws the specified frame of the animation object. This ignores the
        # current playing state.
        #
        # NOTE: If the visibility attribute is False, then nothing will be drawn.
        #
        # @param frameNum
        #     The frame to draw (the first frame is 0, not 1)
        # @param destSurface
        #     The Surface object to draw the frame
        # @param dest
        #     The position to draw the frame. This is passed to Pygame's Surface's
        #     blit() function, so it can be either a (top, left) tuple or a Rect
        #     object.
        if self.isFinished():
            self.state = STOPPED
        if not self.visibility or self.state == STOPPED:
            return
        destSurface.blit(self.getFrame(frameNum), dest)


    def blitFrameAtTime(self, elapsed, destSurface, dest):
        # Draws the frame the is "elapsed" number of seconds into the animation,
        # rather than the time the animation actually started playing.
        #
        # NOTE: If the visibility attribute is False, then nothing will be drawn.
        #
        # @param elapsed
        #     The amount of time into an animation to use when determining which
        #     frame to draw. blitFrameAtTime() uses this parameter rather than
        #     the actual time that the animation started playing. (In seconds)
        # @param destSurface
        #     The Surface object to draw the frame
        # @param dest
        #     The position to draw the frame. This is passed to Pygame's Surface's
        #     blit() function, so it can be either a (top, left) tuple or a Rect
        #     object.        elapsed = int(elapsed * self.rate)
        if self.isFinished():
            self.state = STOPPED
        if not self.visibility or self.state == STOPPED:
            return
        frameNum = findStartTime(self._startTimes, elapsed)
        destSurface.blit(self.getFrame(frameNum), dest)


    def isFinished(self):
        # Returns True if this animation doesn't loop and has finished playing
        # all the frames it has.
        return not self.loop and self.elapsed >= self._startTimes[-1]


    def play(self, startTime=None):
        # Start playing the animation.

        # play() is essentially a setter function for self._state
        # NOTE: Don't adjust the self.state property, only self._state

        if startTime is None:
            startTime = time.time()

        if self._state == PLAYING:
            if self.isFinished():
                # if the animation doesn't loop and has already finished, then
                # calling play() causes it to replay from the beginning.
                self._playingStartTime = startTime
        elif self._state == STOPPED:
            # if animation was stopped, start playing from the beginning
            self._playingStartTime = startTime
        elif self._state == PAUSED:
            # if animation was paused, start playing from where it was paused
            self._playingStartTime = startTime - (self._pausedStartTime - self._playingStartTime)
        self._state = PLAYING

    def stop(self):
        # Reset the animation to the beginning frame, and do not continue playing

        # stop() is essentially a setter function for self._state
        # NOTE: Don't adjust the self.state property, only self._state
        if self._state == STOPPED:
            return # do nothing
        self._state = STOPPED

    def _makeTransformedSurfacesIfNeeded(self):
        # Internal-method. Creates the Surface objects for the _transformedImages list.
        # Don't call this method.
        if self._transformedImages == []:
            self._transformedImages = [surf.copy() for surf in self._images]


    # Transformation methods.
    # (These are analogous to the pygame.transform.* functions, except they
    # are applied to all frames of the animation object.
    def flip(self, xbool, ybool):
        # Flips the image horizontally, vertically, or both.
        # See http://pygame.org/docs/ref/transform.html#pygame.transform.flip
        self._makeTransformedSurfacesIfNeeded()
        for i in range(len(self._images)):
            self._transformedImages[i] = pygame.transform.flip(self.getFrame(i), xbool, ybool)

    # Getter and setter methods for properties
    def _propGetRate(self):
        return self._rate

    def _propSetRate(self, rate):
        rate = float(rate)
        if rate < 0:
            raise ValueError('rate must be greater than 0.')
        self._rate = rate

    rate = property(_propGetRate, _propSetRate)


    def _propGetLoop(self):
        return self._loop

    def _propSetLoop(self, loop):
        if self.state == PLAYING and self._loop and not loop:
            # if we are turning off looping while the animation is playing,
            # we need to modify the _playingStartTime so that the rest of
            # the animation will play, and then stop. (Otherwise, the
            # animation will immediately stop playing if it has already looped.)
            self._playingStartTime = time.time() - self.elapsed
        self._loop = bool(loop)

    loop = property(_propGetLoop, _propSetLoop)


    def _propGetState(self):
        if self.isFinished():
            self._state = STOPPED # if finished playing, then set state to STOPPED.

        return self._state

    def _propSetState(self, state):
        if state not in (PLAYING, PAUSED, STOPPED):
            raise ValueError('state must be one of pyganim.PLAYING, pyganim.PAUSED, or pyganim.STOPPED')
        if state == PLAYING:
            self.play()
        elif state == PAUSED:
            self.pause()
        elif state == STOPPED:
            self.stop()

    state = property(_propGetState, _propSetState)


    def _propGetVisibility(self):
        return self._visibility

    def _propSetVisibility(self, visibility):
        self._visibility = bool(visibility)

    visibility = property(_propGetVisibility, _propSetVisibility)


    def _propSetElapsed(self, elapsed):
        # NOTE: Do to floating point rounding errors, this doesn't work precisely.
        elapsed += 0.00001 # done to compensate for rounding errors
        # TODO - I really need to find a better way to handle the floating point thing.

        # Set the elapsed time to a specific value.
        if self._loop:
            elapsed = elapsed % self._startTimes[-1]

        rightNow = time.time()
        self._playingStartTime = rightNow - (elapsed * self.rate)

        if self.state in (PAUSED, STOPPED):
            self.state = PAUSED # if stopped, then set to paused
            self._pausedStartTime = rightNow


    def _propGetElapsed(self):
        # NOTE: Do to floating point rounding errors, this doesn't work precisely.

        # To prevent infinite recursion, don't use the self.state property,
        # just read/set self._state directly because the state getter calls
        # this method.

        # Find out how long ago the play()/pause() functions were called.
        if self._state == STOPPED:
            # if stopped, then just return 0
            return 0

        if self._state == PLAYING:
            # if playing, then draw the current frame (based on when the animation
            # started playing). If not looping and the animation has gone through
            # all the frames already, then draw the last frame.
            elapsed = (time.time() - self._playingStartTime) * self.rate
        elif self._state == PAUSED:
            # if paused, then draw the frame that was playing at the time the
            # PygAnimation object was paused
            elapsed = (self._pausedStartTime - self._playingStartTime) * self.rate
        if self._loop:
            elapsed = elapsed % self._startTimes[-1]
        elapsed += 0.00001 # done to compensate for rounding errors
        return elapsed

    elapsed = property(_propGetElapsed, _propSetElapsed)

class PygConductor(object):
    def __init__(self, *animations):
        assert len(animations) > 0, 'at least one PygAnimation object is required'

        self._animations = []
        self.add(*animations)


    def add(self, *animations):
        if type(animations[0]) == dict:
            for k in animations[0].keys():
                self._animations.append(animations[0][k])
        elif type(animations[0]) in (tuple, list):
            for i in range(len(animations[0])):
                self._animations.append(animations[0][i])
        else:
            for i in range(len(animations)):
                self._animations.append(animations[i])

    def _propGetAnimations(self):
        return self._animations

    def _propSetAnimations(self, val):
        self._animations = val

    animations = property(_propGetAnimations, _propSetAnimations)

    def play(self, startTime=None):
        if startTime is None:
            startTime = time.time()

        for animObj in self._animations:
            animObj.play(startTime)

    def stop(self):
        for animObj in self._animations:
            animObj.stop()



def findStartTime(startTimes, target):
    # With startTimes as a list of sequential numbers and target as a number,
    # returns the index of the number in startTimes that preceeds target.
    #
    # For example, if startTimes was [0, 2, 4.5, 7.3, 10] and target was 6,
    # then findStartTime() would return 2. If target was 12, returns 4.
    assert startTimes[0] == 0
    lb = 0 # "lb" is lower bound
    ub = len(startTimes) - 1 # "ub" is upper bound

    # handle special cases:
    if len(startTimes) == 0:
        return 0
    if target >= startTimes[-1]:
        return ub - 1

    # perform binary search:
    while True:
        i = int((ub - lb) / 2) + lb

        if startTimes[i] == target or (startTimes[i] < target and startTimes[i+1] > target):
            if i == len(startTimes):
                return i - 1
            else:
                return i

        if startTimes[i] < target:
            lb = i
        elif startTimes[i] > target:
            ub = i
