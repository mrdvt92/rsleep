### rsleep

`rsleep` is an executable which provides random sleep for scripts.

`rsleep` is intended to provide random delays in crontabs so scripts will start after the top of the minute.

### Build

`make`

### RPM

`make rpm`

### Usage in Crontab

```
rsleep 60; echo "do something in the middle of the minute"
```
