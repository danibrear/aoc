(ns day1.core)

(def filename "input1.txt")
(defn calc [mass] (-> mass (/ 3) Math/floor (- 2)))

(defn calc-2 [mass]
  (loop [mass mass sum 0]
    (if (< (calc mass) 0)
      sum
      (recur (calc mass) (+ (calc mass) sum)))))

; Day 1 - Part 1
(with-open [rdr (clojure.java.io/reader "input1.txt")]
  (println (reduce + 0 (map calc (map #(Integer/parseInt %) (line-seq rdr))))))

; Day 1 - Part 2
(with-open [rdr (clojure.java.io/reader "input1.txt")]
  (println (reduce + 0 (map calc-2 (map #(Integer/parseInt %) (line-seq rdr))))))

; (println (reduce + 0 (map calc masses)))