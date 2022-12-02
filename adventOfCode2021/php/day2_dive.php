<?php
// https://adventofcode.com/2021/day/2

function subNavigation($array, $currentPosi){
    $len = count($array);
    $x = $currentPosi[0];
    $y = $currentPosi[1];
    for($i = 0; $i < $len; $i++){
        $curCommand = $array[$i];
        

        if(strpos($curCommand, "forward") == 0){
            str_split($curCommand, 8);
            $x += intval($curCommand[1]);
        }

        if(strpos($curCommand, "down") == 0){
            str_split($curCommand, 5);
            $y += intval($curCommand[1]);
        }

        if(strpos($curCommand, "up") == 0){
            str_split($curCommand, 3);
            $y -= intval($curCommand[1]);
        }
    }
    $z = $x * $y;
    echo $z;
    var_dump($currentPosi);
    return $currentPosi;

}
$currentPosi = [0, 0]; // [x, y]
$array = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"];
subNavigation($array, $currentPosi);
?>