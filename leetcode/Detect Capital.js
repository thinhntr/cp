// https://leetcode.com/problems/detect-capital/
function isCap(char) {
    return char.toLowerCase() !== char;
}
function detectCapitalUse(word) {
    let countCap = 0;
    for (const char of word)
        countCap += isCap(char) ? 1 : 0;
    return countCap === word.length || countCap === 0 || countCap === 1 && isCap(word[0]);
}
class Tester1 {
    constructor(fun) {
        this.time = 0;
        this.total = 0;
        this.fail = 0;
        this.fun = fun;
    }
    test(input, expected) {
        ++this.total;
        const start = performance.now();
        const output = this.fun(input);
        this.time += performance.now() - start;
        const success = output === expected;
        console.log(`Test ${this.total} ... success`);
        if (!success) {
            ++this.fail;
            console.log('Input:', input);
            console.error('Output:', output);
            console.error('Expected:', expected);
        }
        console.log('');
    }
    get pass() {
        return this.total - this.fail;
    }
    report() {
        console.log(`Ran in ${this.time}`);
        console.log(`Passed ${this.pass} / ${this.total} tests.`);
    }
}
const aha = new Tester1(detectCapitalUse);
aha.test('USA', true);
aha.test('Google', true);
aha.test('leetcode', true);
aha.test('FlaG', false);
aha.test('glGr', false);
aha.test('glgR', false);
aha.test('fORREAL', false);
aha.report();
//# sourceMappingURL=Detect%20Capital.js.map