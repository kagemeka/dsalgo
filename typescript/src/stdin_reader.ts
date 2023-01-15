import { readFileSync } from 'fs'

function readSplit(): string[] {
  return readFileSync('/dev/stdin', 'utf-8').split(/ |\n/)
}
function* toGenerator<T>(a: T[]) {
  for (var x of a) {
    yield x
  }
}

// stdin reader
class Reader {
  private chunks: Generator<string>
  constructor() {
    this.chunks = toGenerator(readSplit())
  }
  str(): string {
    return this.chunks.next().value
  }
  int(): number {
    return +this.str()
  }
}
