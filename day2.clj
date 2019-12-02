(ns day2.core
  (:require [clojure.string :as str]))

(def filename "input2.txt")
(def original-input (int-array (map #(Integer/parseInt %) (-> filename slurp (str/split #",")))))
; (def input (int-array [1,9,10,3,2,3,11,0,99,30,40,50]))
; (def input (int-array [2,4,4,5,99,0]))

(defn solve-prob [noun verb]
  (def input (int-array original-input))
  (aset input 1 noun)
  (aset input 2 verb)

  (loop [index 0]
  ;(println "start: " (nth input index) (nth input (+ 1 index)) (nth input (+ 2 index)) (nth input (+ 3 index)))
  ;(println (nth input (+ index 3)) (+ (nth input (nth input (+ index 1))) (nth input (nth input (+ index 2)))))
    (cond
      (= (nth input index) 1) (aset input (nth input (+ index 3)) (+ (nth input (nth input (+ index 1))) (nth input (nth input (+ index 2)))))
      (= (nth input index) 2) (aset input (nth input (+ index 3)) (* (nth input (nth input (+ index 1))) (nth input (nth input (+ index 2))))))
  ;(println "after: " (nth input index) (nth input (+ 1 index)) (nth input (+ 2 index)) (nth input (+ 3 index)))
    (if (= 99 (nth input index)) index (recur (+ index 4))))

  (nth input 0))


(loop [noun 0]
  (loop [verb 0]
    (if (= (solve-prob noun verb) 19690720) (println (+ (* 100 noun) verb)))
    (when (< verb 99) (recur (inc verb))))
  (when (< noun 99) (recur (inc noun))))

; (loop [index 0]
;   (cond 
;     (= (nth input index) 1) (println "one")
;     (= (nth input index) 2) (println "two"))
;   (if (or (= 99 (nth input index)) (> index length)) index (recur (+ index 4))))