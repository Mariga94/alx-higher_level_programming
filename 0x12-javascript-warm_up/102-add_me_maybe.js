#!/usr/bin/node
function addMeMaybe (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}
module.exports = addMeMaybe;
