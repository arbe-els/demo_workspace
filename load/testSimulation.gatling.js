import {
  scenario, rampUsers, simulation, nothingFor, atOnceUsers,
  constantUsersPerSec, incrementUsersPerSec, rampConcurrentUsers, constantConcurrentUsers, rampUsersPerSec,
  incrementConcurrentUsers
} from "@gatling.io/core";
import { http, status } from '@gatling.io/http';

const httpProtocol = http
  .baseUrl("https://demoqa.com/")
  .acceptHeader("text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
  .acceptLanguageHeader("en-US,en;q=0.5")
  .acceptEncodingHeader("gzip, deflate")
  .userAgentHeader("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/115.0");

const scn = scenario("test load web")
  .exec( http("open homepage")
      .get("/")
      .check(status().is(200))
  )
/*export default simulation((setUp) => {
  setUp(
    scn.injectOpen(
      nothingFor(1),
      incrementUsersPerSec(1).times(5).eachLevelLasting(1),
      constantUsersPerSec(15).during(5),
      rampUsersPerSec(15).to(4).during(4),
      rampUsersPerSec(4).to(15).during(4),
      constantUsersPerSec(15).during(5),
      rampUsersPerSec(15).to(1).during(3),
    )
  ).protocols(httpProtocol);
});*/

export default simulation((setUp) => {
  setUp(
    scn.injectClosed(
      incrementConcurrentUsers(1).times(5).eachLevelLasting(1),
      constantConcurrentUsers(15).during(5),
      rampConcurrentUsers(15).to(5).during(4),
      rampConcurrentUsers(5).to(15).during(4),
      constantConcurrentUsers(15).during(5),
      rampConcurrentUsers(15).to(1).during(5)
    )
  ).protocols(httpProtocol);
});