(ns day2.core
  (:require [clojure.string :as str]))

(def filename "input2.txt")
(def original-input (int-array (map #(Integer/parseInt %) (-> filename slurp (str/split #",")))))

(def day-2-value 19690720)

(defn solve-prob [noun verb]
  (def input (int-array original-input))
  (aset input 1 noun)
  (aset input 2 verb)

  (loop [index 0]
    (cond
      (= (nth input index) 1) (aset input (nth input (+ index 3)) (+ (nth input (nth input (+ index 1))) (nth input (nth input (+ index 2)))))
      (= (nth input index) 2) (aset input (nth input (+ index 3)) (* (nth input (nth input (+ index 1))) (nth input (nth input (+ index 2))))))
    (if (= 99 (nth input index)) index (recur (+ index 4))))

  (nth input 0))

(println "Part 1 solution: " (solve-prob 12 2))

(loop [noun 0]
  (loop [verb 0]
    (when (= (solve-prob noun verb) day-2-value) (println "Part 2 solution: " (+ (* 100 noun) verb)))
    (when (< verb 99) (recur (inc verb))))
  (when (< noun 99) (recur (inc noun))))
