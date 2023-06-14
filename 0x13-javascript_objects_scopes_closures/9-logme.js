#!/usr/bin/node

let logTracks = 0;
exports.logMe = function (item) {
  console.log(`${logTracks}: ${item}`);
  logTracks++;
};
