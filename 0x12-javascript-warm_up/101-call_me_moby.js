#!/usr/bin/node

const executeXTimes = (x, theFunction) => {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
exports.executeXTimes = executeXTimes;
