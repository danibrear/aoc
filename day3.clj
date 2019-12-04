(ns day3.core
  (:require [clojure.string :as str]))

(def filename "input3.txt")
(def original-input (-> filename slurp (str/split #"\n")))

(def wires (map #(str/split % #",") original-input))

(defn right [row col count]
  (map (fn [idx] [row (+ col idx)]) (range count)))

(defn left [row col count]
  (map (fn [idx] [row (- col idx)]) (range count)))

(defn up [row col count]
  (map (fn [idx] [(- row idx) col]) (range count)))

(defn down [row col count]
  (map (fn [idx] [(+ row idx) col]) (range count)))

(println "starting")
(def values (for [instruction (first wires)]
              (condp = (first instruction)
                \R (println "right")
                \L (println "left")
                \U (println "up")
                \D (println "down"))))
(println values)
(println "done")