const game = {};

game["suspects"] = [];

game.suspects.push({
  name: "Rusty",
  color: "orange",
});

game.suspects[1] = {
  name: "Miss Scarlet",
  color: "red",
};

const firstColor = game.suspects[0].color;
const secondColor = game.suspects[1].color;

let [color1, color2] = [suspects[0].color, suspects[1].color];

let [{ color: firstColor }, { color: secondColor }] = suspects;

function foo() {
  //   for (let i = 0; i < game.suspects.length; i++) {
  //     console.log(game.suspects[i]);
  //   }
  for (let key in game) {
    console.log(game[key]);
  }
}

var gameloop = function () {
  for (let i = 0; i < game.suspects.length; i++) {
    if (game.suspects[i].name === "Rusty") {
      console.log("Found 'em ");
    } else {
      console.log("Next time!");
    }
  }
};

// foo();
gameloop();
