rule _USSR_0_31__by_Spirit_aclhul
{
	meta:
		description = "USSR 0_31 _ by Spirit"
	strings:
		$a = {E8000000005D83C51255C32083B8ED2037EFC6B979379E8CC930C9E301C3BE32??????B0??30068A064681FE00??????7CF3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
