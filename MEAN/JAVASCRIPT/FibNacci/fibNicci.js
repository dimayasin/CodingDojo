function fib() {
    let fibonacci01 = 0, fibonacci02 = 1;
    function nacci() {
      [fibonacci01, fibonacci02] = [fibonacci02, fibonacci01 + fibonacci02];
      console.log(fibonacci02);
    }
    return nacci
  }
  var fibCounter = fib();
  fibCounter() // should console.log "1"
  fibCounter() // should console.log "1"
  fibCounter() // should console.log "2"
  fibCounter() // should console.log "3"
  fibCounter() // should console.log "5"
  fibCounter() // should console.log "8"