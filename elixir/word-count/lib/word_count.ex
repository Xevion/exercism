defmodule WordCount do
  @splitters String.graphemes(" _!&@:;'\"[]()_=+,$&%^")

  @doc """
  Count the number of words in the sentence.

  Words are compared case-insensitively.
  """
  @spec count(String.t()) :: map
  def count(sentence) do
    sentence
    |> String.downcase()
    |> String.split(@splitters)
    |> Enum.filter(&(String.length(&1) > 0))
    |> Enum.reduce(%{}, fn word, count -> Map.update(count, word, 1, &(&1 + 1)) end)
  end
end
