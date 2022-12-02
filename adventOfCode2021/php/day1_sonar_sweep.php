<?php
// https://adventofcode.com/2021/day/1

function sonarSweep($report){
    $m = count($report);
    $increaseCount = 0;
    for($i = 1; $i < $m; $i++){
        if($report[$i] > $report[$i-1]){
            $increaseCount++;
        }
    }
    return $increaseCount;
}
$test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
echo sonarSweep($test);
?>