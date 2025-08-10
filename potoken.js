import { generate } from "youtube-po-token-generator";
import { createTask } from "youtube-po-token-generator/lib/task.js";

generate().then(console.log, console.error);

const visitorData = "Cgt2WVF4ckU2ZVRvSSjwouHEBjIKCgJCUhIEGgAgQQ%3D%3D"; // Altere esse campo com o seu visitorData
// const visitorData = "..."; // Altere esse campo com o seu visitorData

createTask(visitorData)
  .then((task) => task.start())
  .then(console.log, console.error);
