rule _NeoLite_v1_0_gaweor
{
	meta:
		description = "NeoLite v1_0"
	strings:
		$a = {E99B000000A0}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
