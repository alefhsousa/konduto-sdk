from konduto.infrastructure.either import Right, Either, Left


class TestEither:

    def test_should_return_right(self):
        result = Right('some value')

        assert result.is_right
        assert not result.is_left
        assert result.value == 'some value'
        assert isinstance(result, Either)

    def test_should_return_left(self):
        result = Left('some wrong value')

        assert not result.is_right
        assert result.is_left
        assert result.value == 'some wrong value'
        assert isinstance(result, Either)
