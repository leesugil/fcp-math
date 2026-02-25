# fcp-math
Arithmetic operations and FPS conversions done clean in a FCP-native way.

FCP stores time-related variables in a string format like '100/6000s' representing the fraction value and time unit at the same time. Those variables play crucial rule in everywhere (fps, clip start, clip duration, clip offset, to name a few). Sometimes you want to do some arithmetic calculations with them or convert them properly depending on fps. This package does that.
