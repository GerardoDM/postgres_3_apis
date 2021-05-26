<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Robot;


class RobotController extends Controller
{
    public function index(){

        $robots = Robot::all();
        return $robots;

    }
}
