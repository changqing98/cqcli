import com.google.protobuf.gradle.generateProtoTasks
import com.google.protobuf.gradle.id
import com.google.protobuf.gradle.ofSourceSet
import com.google.protobuf.gradle.plugins
import com.google.protobuf.gradle.protobuf
import com.google.protobuf.gradle.protoc

group = "${group}"
version = "${version}"

plugins {
  java
  idea
  `maven-publish`
  id("com.google.protobuf") version "0.8.10"
}

repositories {
  maven("http://maven.aliyun.com/nexus/content/groups/public/")
  maven("https://plugins.gradle.org/m2/")
}

dependencies {
  compile("com.google.protobuf:protobuf-java:3.10.0")
  compile("io.grpc:grpc-stub:1.23.0")
  compile("io.grpc:grpc-protobuf:1.23.0")
  compile("com.google.api.grpc:grpc-google-common-protos:1.16.0")
  if (JavaVersion.current().isJava9Compatible) {
    // Workaround for @javax.annotation.Generated
    // see: https://github.com/grpc/grpc-java/issues/3633
    compile("javax.annotation:javax.annotation-api:1.3.1")
  }
  testCompile("junit:junit:4.12")
}

protobuf {
  protoc {
    // The artifact spec for the Protobuf Compiler
    artifact = "com.google.protobuf:protoc:3.10.0"
  }
  plugins {
    // Optional: an artifact spec for a protoc plugin, with "grpc" as
    // the identifier, which can be referred to in the "plugins"
    // container of the "generateProtoTasks" closure.
    id("grpc") {
      artifact = "io.grpc:protoc-gen-grpc-java:1.23.0"
    }
  }
  generateProtoTasks {
    ofSourceSet("main").forEach {
      it.plugins {
        // Apply the "grpc" plugin whose spec is defined above, without options.
        id("grpc")
      }
    }
  }
}

val mavenRepositoryUrl: String by project
val mavenRepositoryUsername: String by project
val mavenRepositoryPassword: String by project
val sourcesJar by tasks.registering(Jar::class) {
    archiveClassifier.set("sources")
    from(sourceSets.main.get().allSource)
}

publishing {
  repositories {
    maven(mavenRepositoryUrl) {
      credentials {
        username = mavenRepositoryUsername
        password = mavenRepositoryPassword
      }
    }
  }
  publications {
    register("mavenJava", MavenPublication::class) {
      from(components["java"])
      artifact(sourcesJar.get())
    }
  }
}
