# DESIGN RECIPES

Definitions and cheat sheets for the design recipes of the HtC Recipes.

- [DESIGN RECIPES](#design-recipes)
  - [1. How to Design Functions (HtDF)](#1-how-to-design-functions-htdf)
    - [1. Signature, Purpose and Stub](#1-signature-purpose-and-stub)
    - [2. Define examples, wrap each one in check-expect](#2-define-examples-wrap-each-one-in-check-expect)
    - [3. Template and inventory](#3-template-and-inventory)
    - [4. Code the Function Body](#4-code-the-function-body)
    - [5. Test and debug until correct](#5-test-and-debug-until-correct)
  - [2. How to Design Data (HtDD)](#2-how-to-design-data-htdd)
    - [What is the Inherent Structure of the Information?](#what-is-the-inherent-structure-of-the-information)
    - [Simple Atomic Data](#simple-atomic-data)
    - [Intervals](#intervals)
    - [Enumerations](#enumerations)
    - [Itemizations](#itemizations)
    - [Compound data (structures)](#compound-data-structures)
    - [References to other data definitions](#references-to-other-data-definitions)
    - [Self-referential or mutually referential](#self-referential-or-mutually-referential)

## 1. How to Design Functions (HtDF)

[1.](#1-how-to-design-functions-htdf) Signature, purpose and stub

[2.](#2-define-examples-wrap-each-one-in-check-expect) Define examples, wrap each in check-expect.

[3.](#3-template-and-inventory) Template and inventory.

[4.](#4-code-the-function) Code the function body.

[5.](#5-test-and-debug-until-correct) Test and debug until correct

---

### 1. Signature, Purpose and Stub

Write the function **signature**, a one-line purpose statement and a function stub.

A *signature* has the type of each argument, separated by spaces, followed by `->`, followed by the type of result. So a function that consumes an image and produces a number would have the signature `Image -> Number`.

Note that the **stub** is a syntactically complete function definition that produces a value of the right type. If the type is `Number` it is common to use 0, if the type is `String` it is common to use "a" and so on. The value will not, in general, match the purpose statement. In the example below the stub produces 0, which is a `Number`, but only matches the purpose when double happens to be called with 0.

```racket
;; Number -> Number     ; this is the signature
;; produces n times 2   ; this is the purpose

(define (double n)  0)  ; this is the stub
```

The purpose of the **stub** is to serve as a kind of scaffolding to make it possible to run the examples even before the function design is complete.

With the stub in place `check-expects` that call the function can run. Most of them will fail of course, but the fact that they can run at all allows you to ensure that they are at least well-formed: parentheses are balanced, function calls have the proper number of arguments, function and constant names are correct and so on.

This is very important, the sooner you find a mistake -- even a simple one -- the easier it is to fix.

[Back](#1-how-to-design-functions-htdf)

### 2. Define examples, wrap each one in check-expect

Write at least one **example** of a call to the function and the expected result the call should produce.

You will often need more *examples*, to help you better understand the function or to properly test the function.

If you are unsure how to start writing *examples* use the combination of the function signature and the data definition(s) to help you generate *examples*. Often the example data from the data definition is useful, but it does not necessarily cover all the important cases for a particular function.

The first role of an example is to help you understand what the function is supposed to do. If there are boundary conditions be sure to include an example of them. If there are different behaviours the function should have, include an example of each. Since they are examples first, you could write them in this form:

```racket
;; (double 0) should produce 0
;; (double 1) should produce 2
;; (double 2) should produce 4
```

When you write *examples* it is sometimes helpful to write not just the expected result, but also how it is computed. For example, you might write the following instead of the above:

```racket
;; (double 0) should produce (* 0 2)
;; (double 1) should produce (* 1 2)
;; (double 2) should produce (* 2 2)
```

While the above form satisfies our need for examples, we should enclose them in `check-expect` and turn the examples into unit **tests**.

```racket
;; Number -> Number
;; produces n times 2
(check-expect (double 0) (* 0 2))
(check-expect (double 1) (* 1 2))
(check-expect (double 3) (* 3 2))

(define (double n)  0)  ; this is the stub
```

The existence of the stub will allow you to run the tests. Most (or even all) of the *tests* will fail since the stub is returning the same value every time. But you will at least be able to check that the parentheses are balanced, that you have not misspelled function names etc.

[Back](#1-how-to-design-functions-htdf)

### 3. Template and inventory

Before coding the function body it is helpful to have a clear sense of what the function has to work with -- the **template** provides this.

Once the [How to Design Data Definitions (HtDD)](#2-how-to-design-data-htdd) recipe in introduced, templates are produced by following the rules on the D*ata Driven Templates*. You should copy the template from the data definition to the function design, rename the template, and write a comment that says where the template was copied from. Note that the template is copied from the data definition for the consumed type, not the produced type.

For primitive data like numbers, strings and images the body of the template is simply `(... x)` where `x` is the name of the parameter to the function.

Once the template is done the stub should be commented out.

```racket
;; Number -> Number
;; produces n times 2
(check-expect (double 0) (* 0 2))
(check-expect (double 1) (* 1 2))
(check-expect (double 3) (* 3 2))

;(define (double n) 0) ; this is the stub

(define (double n)     ; this is the template
  (... n))
```

It is also often useful to add constant values which are extremely likely to be useful to the template body at this point. For example, the template for a function that renders the state of a world program might have an `MTS` constant added to its body. This causes the template to include an inventory of useful constants.

[Back](#1-how-to-design-functions-htdf)

### 4. Code the Function Body

Now complete the function body by filling in the template.

Note that:

- the **signature** tells you the type of the parameter(s) and the type of the data the function body must produce
- the **purpose** describes what the function body must produce in English
- the **examples** provide several concrete examples of what the function body must produce
- the **template** tells you the raw material you have to work with

You should use all of the above to help you code the function body. In some cases further rewriting of examples might make it more clear how you computed certain values, and that may make it easier to code the function.

```racket
;; Number -> Number
;; produces n times 2
(check-expect (double 0) (* 0 2))
(check-expect (double 1) (* 1 2))
(check-expect (double 3) (* 3 2))

;(define (double n) 0) ; this is the stub

;(define (double n)    ; this is the template
;  (... n))

(define (double n)
  (* n 2))
```

[Back](#1-how-to-design-functions-htdf)

### 5. Test and debug until correct

Run the program and make sure all the tests pass, if not debug until they do. Many of the problems you might have had will already have been fixed because of following the "run early, run often" approach. But if not, debug until everything works.

[Back](#1-how-to-design-functions-htdf)

---

## 2. How to Design Data (HtDD)

Data definitions are a **driving element** in the design recipes.

A data definition establishes the *represent/interpret* relationship between information and data:

- **Information** in the program's domain is *represented by data* in the program.
- **Data** in the program can be *interpreted as information* in the program's domain.

A **data definition** must describe how to form (or make) data that satisfies the data definition and also how to tell whether a data value satisfies the data definition. It must also describe how to represent information in the program's domain as data and interpret a data value as information.

So, for example, one data definition might say that numbers are used to represent the Speed of a ball. Another data definition might say that numbers are used to represent the Height of an airplane. So given a number like 6, we need a data definition to tell us how to interpret it: is it a Speed, or a Height or something else entirely. Without a data definition, the 6 could mean anything.

The first step of the recipe is to identify the inherent structure of the information.

Once that is done, a data definition consists of four or five elements:

1. A possible **structure definition** (not until compound data)
2. A **type comment** that defines a new type name and describes how to form data of that type.
3. An **interpretation** that describes the correspondence between information and data.
4. One or more **examples** of the data.
5. A **template** for a 1 argument function operating on data of this type.

[Back](#design-recipes)

---

### What is the Inherent Structure of the Information?

One of the most important points in the course is that:

- the **structure of the information** in the program's domain determines the kind of data definition used,
- which in turn determines the **structure of the templates** and helps determine the function examples (check-expects),
- and therefore the **structure of much of the final program design**.

The remainder of this page lists in detail different kinds of data definition that are used to represent information with different structures. The page also shows in detail how to design a data definition of each kind. This summary table provides a quick reference to which kind of data definition to use for different information structures.

| When the form of the information to be represented...                              | Use a data definition of this kind                       |
|------------------------------------------------------------------------------------|----------------------------------------------------------|
| is atomic                                                                          | [Simple Atomic Data](#simple-atomic-data)                |
| is numbers within a certain range                                                  | [Interval](#intervals)                                   |
| consists of a fixed number of distinct items                                       | [Enumeration](#enumerations)                             |
| is comprised of 2 or more subclasses, at least one of which is not a distinct item | [Itemization](#itemizations)                             |
| consists of two or more items that naturally belong together                       | [Compound data](#compound-data-structures)               |
| is naturally composed of different parts                                           | [References to other defined type](#references-to-other-data-definitions)|
| is of arbitrary (unknown) size                                                     | [self-referential or mutually referential](#self-referential-or-mutually-referential)|

[Back](#design-recipes)

---

### Simple Atomic Data

Use simple atomic data **when the information to be represented is itself atomic in form**, such as the elapsed time since the start of the animation, the x coordinate of a car or the name of a cat.

```racket
;; Time is Natural
;; interp. number of clock ticks since start of game

(define START-TIME 0)
(define OLD-TIME 1000)

#;
(define (fn-for-time t)
  (... t))

;; Template rules used:
;;  - atomic non-distinct: Natural
```

**Forming the Template:**

As noted below the template, it is formed according to the [Data Driven Templates recipe](#) using the right hand column of the atomic non-distinct rule.

**Guidance on Data Examples and Function Example/Tests:**

One or two data examples are usually sufficient for simple atomic data.

When creating example/tests for a specific function operating on simple atomic data at least one test case will be required. Additional tests are required if there are multiple cases involved. If the function produces Boolean there needs to be at least a true and false test case. Also be on the lookout for cases where a number of some form is an [interval]((#intervals)) in disguise, for example given a type comment like Countdown is Natural, in some functions 0 is likely to be a special case.

[Back](#design-recipes)

---

### Intervals

Use an interval when the information to be represented is numbers within a certain range. `Integer[0, 10]` is all the integers from 0 to 10 inclusive; `Number[0, 10)` is all the numbers from 0 inclusive to 10 exclusive. (The notation is that [ and ] mean that the end of the interval includes the end point; ( and ) mean that the end of the interval does not include the end point.)

Intervals often appear in [itemizations](#itemizations), but can also appear alone, as in:

```racket
;; Countdown is Integer[0, 10]
;; interp. the number of seconds remaining to liftoff
(define C1 10)  ; start
(define C2 5)   ; middle
(define C3 0)   ; end
 
#;
(define (fn-for-countdown cd)
  (... cd))

;; Template rules used:
;;  - atomic non-distinct: Integer[0, 10]
```

**Forming the Template:**

As noted below the template, it is formed according to the [Data Driven Templates recipe](#) using the right hand column of the atomic non-distinct rule.

**Guidance on Data Examples and Function Example/Tests:**

For data examples provide sufficient examples to illustrate how the type represents information. The three data examples above are probably more than is needed in that case.

When writing tests for functions operating on intervals be sure to test closed boundaries as well as midpoints. As always, be sure to include enough tests to check all other points of variance in behaviour across the interval.

[Back](#design-recipes)

---

### Enumerations

Use an enumeration **when the information to be represented consists of a fixed number of distinct items**, such as colors, letter grades etc. The data used for an enumeration could in principle be anything - strings, integers, images even. But we always use strings. In the case of enumerations it is sometimes redundant to provide an interpretation and nearly always redundant to provide examples. The example below includes the interpretation but not the examples.

```racket
;; LightState is one of:
;;  - "red"
;;  - "yellow"
;;  - "green"
;; interp. the color of a traffic light

;; <examples are redundant for enumerations>
 
#;
(define (fn-for-light-state ls)
  (cond [(string=? "red" ls) (...)]
        [(string=? "yellow" ls) (...)]
        [(string=? "green" ls) (...)]))
;; Template rules used:
;;  - one of: 3 cases
;;  - atomic distinct: "red"
;;  - atomic distinct: "yellow"
;;  - atomic distinct: "green"
```

**Forming the Template:**

As noted below the template, it is formed according to the [Data Driven Templates recipe](#) as follows:

First, `LightState` is an enumeration with 3 cases, so the *one of rule* says to use a cond with 3 cases:

```racket
(define (fn-for-tlcolor ls)
  (cond [Q1 A1]
        [Q2 A2]
        [Q3 A3])) 
```

In the first clause, `"red"` is a distinct atomic value, so the cond question column of the `atomic distinct rule` says Q1 should be `(string=? ls "red")`. The cond answer column says A1 should be `(...)`. So we have:

```racket
(define (fn-for-light-state ls)
  (cond [(string=? "red" ls) (...)]
        [Q2 A2]
        [Q3 A3])) 
```

Then `"yellow"` and `"green"` are also distinct atomic values, so the final template is:

```racket
(define (fn-for-light-state ls) 
  (cond [(string=? "red" ls) (...)]
        [(string=? "yellow" ls) (...)]
        [(string=? "green" ls) (...)]))
```

**Guidance on Data Examples and Function Example/Tests:**

Data examples are redundant for enumerations.

Functions operating on enumerations should have (at least) as many tests as there are cases in the enumeration.

**Large Enumerations:**

Some enumerations contain a large number of elements. A canonical example is KeyEvent, which is provided as part of big-bang. KeyEvent includes all the letters of the alphabet as well as other keys you can press on the keyboard. It is not necessary to write out all the cases for such a data definition. Instead write one or two, as well as a comment saying what the others are, where they are defined etc.

Defer writing templates for such large enumerations until a template is needed for a specific function. At that point include the specific cases that function cares about. Be sure to include an else clause in the template to handle the other cases. As an example, some functions operating on KeyEvent may only care about the space key and just ignore all other keys, the following would be an appropriate template for such functions.

```racket
#;
(define (fn-for-key-event kevt)
  (cond [(key=? " " kevt) (...)]
        [else
         (...)]))
;; Template formed using the large enumeration special case
```

The same is true of writing tests for functions operating on large enumerations. All the specially handled cases must be tested, in addition one more test is required to check the else clause.

[Back](#design-recipes)

---

### Itemizations

An itemization describes **data comprised of 2 or more subclasses, at least one of which is not a distinct item**. (C.f. enumerations, where the subclasses are **all** distinct items.) In an itemization the template is similar to that for enumerations: a cond with one clause per subclass. In cases where the subclass of data has its own data definition the answer part of the cond clause includes a call to a helper template, in other cases it just includes the parameter.

```racket
;; Bird is one of:
;;  - false
;;  - Number
;; interp. false means no bird, number is x position of bird

(define B1 false)
(define B2 3) 

#;
(define (fn-for-bird b)
  (cond [(false? b) (...)]
        [(number? b) (... b)]))
;; Template rules used:
;;  - one of: 2 cases
;;  - atomic distinct: false
;;  - atomic non-distinct: Number
```

**Forming the Template:**

As noted below the template, it is formed according to the [Data Driven Templates recipe](#) using the *one-of rule*, the *atomic distinct rule* and the *atomic non-distinct rule* in order.

**Guidance on Data Examples and Function Example/Tests:**

As always, itemizations should have enough data examples to clearly illustrate how the type represents information.

Functions operating on itemizations should have at least as many tests as there are cases in the itemizations. If there are intervals in the itemization, then there should be tests at all points of variance in the interval. In the case of adjoining intervals it is critical to test the boundaries.

**Itemization of Intervals:**

A common case is for the itemization to be comprised of 2 or more intervals. In this case functions operating on the data definition will usually need to be tested at all the boundaries of closed intervals and points between the boundaries.

```racket
;;; Reading is one of:
;;  - Number[> 30]      
;;  - Number(5, 30]     
;;  - Number[0, 5]      
;; interp. distance in centimeters from bumper to obstacle
;;    Number[> 30]    is considered "safe"
;;    Number(5, 30]   is considered "warning"
;;    Number[0, 5]    is considered "dangerous"
(define R1 40)
(define R2 .9)

(define (fn-for-reading r)
  (cond [(< 30 r) (... r)]
        [(and (<  5 r) (<= r  30)) (... r)]
        [(<= 0 r 5) (... r)]))

;; Template rules used:
;;  one-of: 3 cases
;;  atomic non-distinct:  Number[>30]
;;  atomic non-distinct:  Number(5, 30]
;;  atomic non-distinct:  Number[0, 5]
```

As noted below the template, it is formed according to the [Data Driven Templates recipe](#) using the *one-of rule*, followed by 3 uses of the *atomic non-distinct rule*.

[Back](#design-recipes)

---

### Compound data (structures)

Use structures when two or more values naturally belong together. The define-struct goes at the beginning of the data definition, before the types comment.

```racket
(define-struct ball (x y))
;; Ball is (make-ball Number Number)
;; interp. a ball at position x, y 

(define BALL-1 (make-ball 6 10))

#;
(define (fn-for-ball b)
  (... (ball-x b)     ;Number
       (ball-y b)))   ;Number
;; Template rules used:
;;  - compound: 2 fields
```

The template above is formed according to the [Data Driven Templates recipe](#) using the compound rule. Then for each of the selectors, the result type of the selector (Number in the case of ball-x and ball-y) is used to decide whether the selector call itself should be wrapped in another expression. In this case, where the result types are primitive, no additional wrapping occurs. C.f. cases below when the reference rule applies.

**Guidance on Data Examples and Function Example/Tests:**

For compound data definitions it is often useful to have numerous examples, for example to illustrate special cases. For a snake in a snake game you might have an example where the snake is very short, very long, hitting the edge of a box, touching food etc. These data examples can also be useful for writing function tests because they save space in each check-expect.

[Back](#design-recipes)

---

### References to other data definitions

Some data definitions contain references to other data definitions you have defined (non-primitive data definitions). One common case is for a compound data definition to comprise other named data definitions. (Or, once lists are introduced, for a list to contain elements that are described by another data definition. In these cases the template of the first data definition should contain calls to the second data definition's template function wherever the second data appears. For example:

```racket
---assume Ball is as defined above---

(define-struct game (ball score))
;; Game is (make-game Ball Number) 

;; interp. the current ball and score of the game

(define GAME-1 (make-game (make-ball 1 5) 2))

#;
(define (fn-for-game g)
  (... (fn-for-ball (game-ball g))
       (game-score g)))      ;Number
;; Template rules used:
;;  - compound: 2 fields
;;  - reference: ball field is Ball
```

In this case the template is formed according to the [Data Driven Templates recipe](#) by first using the *compound rule*. Then, since the result type of `(game-ball g)` is `Ball`, the *reference rule* is used to wrap the selector so that it becomes `(fn-for-ball (game-ball g))`. The call to `game-score` is not wrapped because it produces a primitive type.

**Guidance on Data Examples and Function Example/Tests:**

For data definitions involving references to non-primitive types the data examples can sometimes become quite long. In these cases it can be helpful to define well-named constants for data examples for the referred to type and then use those constants in the referring from type. For example:

```racket
...in the data definition for Drop...
(define DTOP (make-drop 10 0))            ;top of screen
(define DMID (make-drop 20 (/ HEIGHT 2))) ;middle of screen
(define DBOT (make-drop 30 HEIGHT))       ;at bottom edge
(define DOUT (make-drop 40 (+ HEIGHT 1))) ;past bottom edge

...in the data definition for ListOfDrop...
(define LOD1 empty)
(define LOD-ALL-ON             (cons DTOP (cons DMID )))
(define LOD-ONE-ABOUT-TO-LEAVE (cons DTOP (cons DMID (cons DBOT empty))))
(define LOD-ONE-OUT-ALREADY    (cons DTOP (cons DMID (cons DBOT (cons DOUT empty)))))
```

In the case of references to non-primitive types the function operating on the referring type (i.e. `ListOfDrop`) will end up with a call to a helper that operates on the referred to type (i.e. `Drop`). Tests on the helper function should fully test that function, tests on the calling function may assume the helper function works properly.

[Back](#design-recipes)

---

### Self-referential or mutually referential

When the **information in the program's domain is of arbitrary size**, a well-formed self-referential (or mutually referential) data definition is needed.

In order to be well-formed, a self-referential data definition must:

1. have at least one case without self reference (the base case(s))
2. have at least one case with self reference

The template contains a base case corresponding to the non-self-referential clause(s) as well as one or more natural recursions corresponding to the self-referential clauses.

```racket
;; ListOfString is one of:
;;  - empty
;;  - (cons String ListOfString)
;; interp. a list of strings

(define LOS-1 empty)
(define LOS-2 (cons "a" empty))
(define LOS-3 (cons "b" (cons "c" empty)))

#;
(define (fn-for-los los)
  (cond [(empty? los) (...)]                   ;BASE CASE
        [else (... (first los)                 ;String
                   (fn-for-los (rest los)))])) ;NATURAL RECURSION
;;             /
;;            /
;;       COMBINATION
;; Template rules used:
;;  - one of: 2 cases
;;  - atomic distinct: empty
;;  - compound: (cons String ListOfString)
;;  - self-reference: (rest los) is ListOfString
```

In some cases a types comment can have both self-reference and reference to another type.

```racket
(define-struct dot (x y))
;; Dot is (make-dot Integer Integer)
;; interp. A dot on the screen, w/ x and y coordinates.
(define D1 (make-dot 10 30))
#;
(define (fn-for-dot d)
  (... (dot-x d)   ;Integer
       (dot-y d))) ;Integer
;; Template rules used:
;;  - compound: 2 fields

;; ListOfDot is one of:
;;  - empty
;;  - (cons Dot ListOfDot)
;; interp. a list of Dot
(define LOD1 empty)
(define LOD2 (cons (make-dot 10 20) (cons (make-dot 3 6) empty)))
#;
(define (fn-for-lod lod)
  (cond [(empty? lod) (...)]
        [else
         (... (fn-for-dot (first lod))
              (fn-for-lod (rest lod)))]))

;; Template rules used:
;;  - one of: 2 cases
;;  - atomic distinct: empty
;;  - compound: (cons Dot ListOfDot)
;;  - reference: (first lod) is Dot 
;;  - self-reference: (rest lod) is ListOfDot
```

**Guidance on Data Examples and Function Example/Tests:**

When writing data and function examples for self-referential data definitions always put the base case first. Its usually trivial for data examples, but many function tests don't work properly if the base case isn't working properly, so testing that first can help avoid being confused by a failure in a non base case test. Also be sure to have a test for a list (or other structure) that is at least 2 long.

[Back](#design-recipes)

---
