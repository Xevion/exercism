(ns armstrong-numbers)

; (defn armstrong? [num]
;   (let [x (clojure.string/split (str num) #"")
;         x (mapv read-string x)
;         x (mapv #(* % %) x)
;       ]
;     (
;       (prn x)
;     )
;   )
; )

(defn armstrong? [num] "ye")

(defn main [& args]
  (armstrong? 9119)
)