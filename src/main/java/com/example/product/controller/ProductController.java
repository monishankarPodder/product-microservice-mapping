package com.example.product.controller;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/product")
public class ProductController {

    @GetMapping("/hello")
    public String hello() {
        return "Hello Product Service13!";
    }
}
