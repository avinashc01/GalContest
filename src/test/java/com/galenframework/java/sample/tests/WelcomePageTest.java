package com.galenframework.java.sample.tests;

import com.galenframework.java.sample.components.GalenTestBase;
import org.openqa.selenium.By;
import org.testng.annotations.Test;
import java.io.IOException;


public class WelcomePageTest extends GalenTestBase {

    @Test(dataProvider = "devices")
    public void welcomePage(TestDevice device) throws IOException {
        load("/");
        checkLayout("/specs/welcomePageNew.spec", device.getTags());
    }

}
