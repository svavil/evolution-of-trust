# evolution-of-trust
A Python implementation of the iterated prisoner's dilemma, inspired by the 'Evolution of Trust' by Nicky Case ([game](https://ncase.me/trust/), [github](https://github.com/ncase/trust)).

Run by evaluating `print_statistics` on a list of bots, such as
```
print_statistics([AlwaysBetray(), AlwaysCooperate(), Copycat(), Random()])
```
This should return a (non-deterministic) score table, higher is better, such as
```
378     AlwaysBetray
253     Random
203     Copycat
134     AlwaysCooperate
```

Pull requests that add more bots are welcome.
