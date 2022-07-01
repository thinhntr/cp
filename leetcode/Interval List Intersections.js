// https://leetcode.com/problems/interval-list-intersections/

/**
 * @param {number[][]} firstList
 * @param {number[][]} secondList
 * @return {number[][]}
 */
var intervalIntersection = function (firstList, secondList) {
  const intersections = []
  const [N1, N2] = [firstList.length, secondList.length]
  let [i1, i2] = [0, 0]

  while (i1 < N1 && i2 < N2) {
    const [s1, e1] = [firstList[i1][0], firstList[i1][1]]
    const [s2, e2] = [secondList[i2][0], secondList[i2][1]]

    if (s1 <= s2 && s2 <= e1) {
      intersections.push([s2, Math.min(e1, e2)])
    } else if (s2 <= s1 && s1 <= e2) {
      intersections.push([s1, Math.min(e1, e2)])
    }

    if (e1 < e2) ++i1
    else if (e1 > e2) ++i2
    else {
      ++i1
      ++i2
    }
  }

  return intersections
}
