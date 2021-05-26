'use strict'

const Robot = use('App/Models/Robot');


class RobotController {

    async index(){

        let robots = await Robot.all()
        return robots
    }

    async create({request}){
        const { id,nombre} = await request.all();
        const robot = new Robot();
        robot.fill({
            id,
            nombre,
        });

        await robot.save()
        return robot;
    }
}

module.exports = RobotController
