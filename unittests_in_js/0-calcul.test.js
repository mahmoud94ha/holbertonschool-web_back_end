const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber for ROUNDING AND SUM', () => {
  it('should return the sum of rounded numbers', () => {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    assert.strictEqual(calculateNumber('SUM', 2.8, 2), 5);
    assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
    assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
    assert.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
    assert.strictEqual(calculateNumber('SUM', 1.5, 1.2), 3);
  });
});

describe('calculateNumber for SUBTRACTION', () => {
  it('should return the result of subtraction', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 3, 1), 2);
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -3);
    assert.strictEqual(calculateNumber('SUBTRACT', 4.5, 1.4), 3);
  });
});

describe('calculateNumber for DIVISION', () => {
  it('should return the result of division', () => {
    assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.3);
    assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });
});