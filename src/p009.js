
class Triplet {
  constructor(args) {
    this.sum = args.sum
    this.regArray = []
    this.combinationArray = []
    this.answer = 0
    this.count = 1

    this.getNextSquares()
    this.getAnswer()
  }

  getNextSquares() {
    this.regArray.push(this.count)
    this.count++
  }

  runCombinations() {
    for (let aIndex = 0; aIndex < this.regArray.length - 2; aIndex++) {
      const a = this.regArray[aIndex];

      for (let bIndex = aIndex + 1; bIndex < this.regArray.length - 1; bIndex++) {
        const b = this.regArray[bIndex];

        for (let cIndex = this.regArray.length - 1; cIndex < this.regArray.length; cIndex++) {
          const c = this.regArray[cIndex];
          var value = a + b + c
          if (value === this.sum) {
            this.combinationArray.push([a, b, c])
            if (a * a + b * b === c * c) {
              this.answer = a * b * c
            }
          } else if (value > this.sum) {
            break;
          }
        }
      }

    }
  }

  getAnswer() {
    while (!this.answer) {
      this.getNextSquares()
      this.runCombinations()
    }
  }
}
console.time('timer')
let triplet = new Triplet({
  sum: 1000
})
console.timeEnd('timer')
console.log(triplet.answer)

