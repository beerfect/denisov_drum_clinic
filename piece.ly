\version "2.20.0" 

\header{
    title = "Triplets by 5 in 4/4"
    subtitle = "notes grouping = '10100'"
    subsubtitle = "offset = 0"
    composer = "Dmitriy Denisov"  
}

\layout {
    indent = #0
}

\markup {
    Note filling
}

\relative c'{
\set fontSize = 1
\clef percussion 
\stemUp

\time 4/4
\repeat volta 4 {

	\tuplet 3/2 {d8^> d8   d8^> } \tuplet 3/2 {d8   d8   d8^> } \tuplet 3/2 {d8   d8^> d8   } \tuplet 3/2 {d8   d8^> d8   } 
	\tuplet 3/2 {d8^> d8   d8   } \tuplet 3/2 {d8^> d8   d8^> } \tuplet 3/2 {d8   d8   d8^> } \tuplet 3/2 {d8   d8^> d8   } 
	\tuplet 3/2 {d8   d8^> d8   } \tuplet 3/2 {d8^> d8   d8   } \tuplet 3/2 {d8^> d8   d8^> } \tuplet 3/2 {d8   d8   d8^> } 
	\tuplet 3/2 {d8   d8^> d8   } \tuplet 3/2 {d8   d8^> d8   } \tuplet 3/2 {d8^> d8   d8   } \tuplet 3/2 {d8^> d8   d8^> } 
	\tuplet 3/2 {d8   d8   d8^> } \tuplet 3/2 {d8   d8^> d8   } \tuplet 3/2 {d8   d8^> d8   } \tuplet 3/2 {d8^> d8   d8   } 
	\tuplet 3/2 {d8^> d8   d8^> } \tuplet 3/2 {d8   d8   d8^> } \tuplet 3/2 {d8   d8^> d8   } \tuplet 3/2 {d8   d8^> d8   } 
	\tuplet 3/2 {d8^> d8   d8   } \tuplet 3/2 {d8^> d8   d8^> } \tuplet 3/2 {d8   d8   d8^> } \tuplet 3/2 {d8   d8^> d8   } 
	\tuplet 3/2 {d8   d8^> d8   } \tuplet 3/2 {d8^> d8   d8   } \tuplet 3/2 {d8^> d8   d8^> } \tuplet 3/2 {d8   d8   d8^> } 

  }
}

\markup {
    No filling
}

\relative c'{
\set fontSize = 1
\clef percussion 
\stemUp

\time 4/4
\repeat volta 4 {

	\tuplet 3/2 {d4 d8 } \tuplet 3/2 {r4 d8 } \tuplet 3/2 {r8 d8 r8 } \tuplet 3/2 {r8 d8 r8 } 
	d4 \tuplet 3/2 {d4 d8 } \tuplet 3/2 {r4 d8 } \tuplet 3/2 {r8 d8 r8 } 
	\tuplet 3/2 {r8 d8 r8 } d4 \tuplet 3/2 {d4 d8 } \tuplet 3/2 {r4 d8 } 
	\tuplet 3/2 {r8 d8 r8 } \tuplet 3/2 {r8 d8 r8 } d4 \tuplet 3/2 {d4 d8 } 
	\tuplet 3/2 {r4 d8 } \tuplet 3/2 {r8 d8 r8 } \tuplet 3/2 {r8 d8 r8 } d4 
	\tuplet 3/2 {d4 d8 } \tuplet 3/2 {r4 d8 } \tuplet 3/2 {r8 d8 r8 } \tuplet 3/2 {r8 d8 r8 } 
	d4 \tuplet 3/2 {d4 d8 } \tuplet 3/2 {r4 d8 } \tuplet 3/2 {r8 d8 r8 } 
	\tuplet 3/2 {r8 d8 r8 } d4 \tuplet 3/2 {d4 d8 } \tuplet 3/2 {r4 d8 } 

  }
}