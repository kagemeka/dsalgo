# dsalgo Dart

## development

### Setup & CI

prerequisites

- ubuntu/debian
  - amd64/arm64

```sh
./ci.sh
source ~/.bashrc
```

### VSCode Extensions

- Dart

### compilation

```sh
dart compile exe main.dart -o run
./run
```

### commands

- <https://dart.dev/tools/dart-tool>
check full commands

```sh
dart -v
```

### format

- see all options

```sh
dart format -v
```

### lint

add `lints` package

```sh
 dart pub add --dev lints

```

- <https://dart.dev/guides/language/analysis-options>
- <https://dart.dev/tools/linter-rules#error-rules>

### test

- <https://dart.dev/guides/testing>
- <https://pub.dev/packages/test>
