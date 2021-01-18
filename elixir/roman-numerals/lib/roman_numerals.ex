defmodule RomanNumerals do
  @values %{
    "I" => 1,
    "IV" => 4,
    "V" => 5,
    "IX" => 9,
    "X" => 10,
    "XL" => 40,
    "L" => 50,
    "XC" => 90,
    "C" => 100,
    "CD" => 400,
    "D" => 500,
    "CM" => 900,
    "M" => 1000
  }

  @doc """
  Convert the number to a roman number.
  """
  @spec numeral(pos_integer) :: String.t()
  def numeral(number) do
    number
    |> Stream.unfold(fn
      0 -> nil
      n -> get_max(n)
    end)
    |> Enum.join()
  end

  defp get_max(n) do
    numeral =
      Map.keys(@values)
      |> Enum.filter(&(Map.get(@values, &1) <= n))
      |> Enum.max_by(&Map.get(@values, &1))

    {numeral, n - Map.get(@values, numeral)}
  end
end
