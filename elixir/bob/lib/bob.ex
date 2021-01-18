defmodule Bob do
  def hey(input) do
    input = String.trim(input)

    uppercase =
      Enum.all?(
        Enum.filter(String.graphemes(input), &String.match?(&1, ~r/^\p{L}$/u)),
        &String.match?(&1, ~r/^\p{Lu}$/u)
      )

    has_letters = Enum.any?(String.graphemes(input), &String.match?(&1, ~r/^\p{L}$/u))
    question = String.ends_with?(input, "?")

    cond do
      String.length(input) == 0 ->
        "Fine. Be that way!"

      has_letters && uppercase && question ->
        "Calm down, I know what I'm doing!"

      question ->
        "Sure."

      has_letters && uppercase ->
        "Whoa, chill out!"

      true ->
        "Whatever."
    end
  end
end
