#!/usr/bin/node

const addMeMaybe = (number, theFunction) => {
  const addMeMaybe = number + 1;
  theFunction(incrementedNumber);
};

exports.addMeMaybe = addMeMaybe;
