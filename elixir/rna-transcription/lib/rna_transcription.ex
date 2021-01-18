defmodule RnaTranscription do
  # Turns all 1-item charlist keys and values inside the base map into integers
  @transcription %{'G' => 'C', 'C' => 'G', 'T' => 'A', 'A' => 'U'}
                 |> Enum.map(fn {k, v} -> {List.first(k), List.first(v)} end)
                 |> Enum.into(%{})

  @doc """
  Transcribes a character list representing DNA nucleotides to RNA

  ## Examples

  iex> RnaTranscription.to_rna('ACTG')
  'UGAC'
  """
  @spec to_rna([char]) :: [char]
  def to_rna(dna) do
    dna |> Enum.map(fn x -> Map.get(@transcription, x) end)
  end
end
