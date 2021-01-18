defmodule BeerSong do
  @basic "~s bottle~s of beer on the wall, ~s bottle~s of beer.\n~s, ~s bottle~s of beer on the wall.~n"
  @take "Take ~s down and pass it around"
  @store "Go to the store and buy some more"

  @doc """
  Get a single verse of the beer song
  """
  @spec verse(integer) :: String.t()
  def verse(number) do
    :io_lib.format(@basic, get_args(number)) |> to_string()
  end

  @doc """
  Get the entire beer song for a given range of numbers of bottles.
  """
  @spec lyrics(Range.t()) :: String.t()
  def lyrics(), do: lyrics(99..0)

  def lyrics(range) do
    range |> Enum.map(&verse(&1)) |> Enum.join("\n")
  end

  defp get_args(number) do
    cond do
      number == 0 ->
        ["No more", "s", "no more", "s", @store, "99", "s"]

      number == 1 ->
        ["1", "", "1", "", :io_lib.format(@take, ["it"]) |> to_string(), "no more", "s"]

      number == 2 ->
        ["2", "s", "2", "s", :io_lib.format(@take, ["one"]) |> to_string(), "1", ""]

      true ->
        [
          "#{number}",
          "s",
          "#{number}",
          "s",
          :io_lib.format(@take, ["one"]) |> to_string(),
          "#{number - 1}",
          "s"
        ]
    end
  end
end
