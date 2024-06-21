%% Stewart Platform
% This model shows a Stewart platform manipulator that can track a
% parameterized reference trajectory. The shape, size, and kinematics of
% the manipulator are highly configurable.
% 
% The reference trajectory is specified in 6-D pose space, and an inverse
% kinematics module converts it into one through 6-D leg position space.  A
% generic PID controller attempts to drive the manipulator along the
% desired trajectory.
%
% Copyright 2023 The MathWorks, Inc.

open_system('StewartPlatform');
%%
close_system('StewartPlatform');