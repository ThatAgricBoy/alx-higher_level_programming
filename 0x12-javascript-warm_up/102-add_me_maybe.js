#!/usr/bin/node

const addMeMaybe = (number, theFunction) => {
  const addMeMaybe = number ++;
  theFunction(addMeMaybe);
};

exports.addMeMaybe = addMeMaybe;
