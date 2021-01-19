defmodule RobotSimulator do
  defmodule Robot, do: defstruct([:position, :direction])

  @directions [:north, :east, :south, :west]
  @turns %{"R" => 1, "L" => -1}

  defguardp is_direction(direction) when direction in [:north, :east, :south, :west]

  defguardp is_position(position)
            when is_tuple(position) and tuple_size(position) == 2 and
                   is_integer(elem(position, 0)) and is_integer(elem(position, 1))

  @doc """
  Create a Robot Simulator given an initial direction and position.

  Valid directions are: `:north`, `:east`, `:south`, `:west`
  """
  @spec create(direction :: atom, position :: {integer, integer}) :: any
  def create(direction \\ :north, position \\ {0, 0})

  def create(direction, _position) when not is_direction(direction),
    do: {:error, "invalid direction"}

  def create(_direction, position) when not is_position(position),
    do: {:error, "invalid position"}

  def create(direction, position) do
    %Robot{position: position, direction: direction}
  end

  @doc """
  Simulate the robot's movement given a string of instructions.

  Valid instructions are: "R" (turn right), "L", (turn left), and "A" (advance)
  """
  @spec simulate(robot :: any, instructions :: String.t()) :: any
  def simulate(robot, ""), do: robot

  def simulate(
        %Robot{position: position, direction: direction} = robot,
        <<head::bytes-size(1)>> <> tail
      ) do
    # {head, tail} = String.split_at(instructions, 1)

    case head do
      "A" ->
        # Map.get_and_update!(robot, :position, &{&1, get_change(&1, robot.direction)})
        simulate(%Robot{robot | position: get_change(position, direction)}, tail)

      "L" ->
        simulate(%Robot{robot | direction: get_turn(head, direction)}, tail)

      "R" ->
        simulate(%Robot{robot | direction: get_turn(head, direction)}, tail)

      _ ->
        {:error, "invalid instruction"}
    end
  end

  @doc """
  Return the robot's direction.

  Valid directions are: `:north`, `:east`, `:south`, `:west`
  """
  @spec direction(robot :: any) :: atom
  def direction(robot) do
    robot.direction
  end

  @doc """
  Return the robot's position.
  """
  @spec position(robot :: any) :: {integer, integer}
  def position(robot) do
    robot.position
  end

  def get_turn(turn, direction) do
    @directions
    |> Enum.fetch(rem(Enum.find_index(@directions, &(&1 == direction)) + @turns[turn], 4))
    |> elem(1)
  end

  def get_change({x, y}, direction) do
    case direction do
      :north -> {x, y + 1}
      :east -> {x + 1, y}
      :south -> {x, y - 1}
      :west -> {x - 1, y}
    end
  end
end
