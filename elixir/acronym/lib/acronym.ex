defmodule Acronym do
  @doc """
  Generate an acronym from a string.
  "This is a string" => "TIAS"
  """
  @spec abbreviate(String.t()) :: String.t()
  def abbreviate(string) do
    string
    |> String.split(~r/\s|[-]|(?<=[a-z])-(?=[A-Z])|(?<=[a-z])(?=[A-Z])/)
    |> Enum.filter(&String.match?(&1, ~r/^\w/))
    |> Enum.map(&String.upcase(String.at(String.trim(&1, "_"), 0)))
    |> Enum.join("")
  end
end
