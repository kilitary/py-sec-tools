rule _ASPack_v1_08_x_ujddek
{
	meta:
		description = "ASPack v1_08_x"
	strings:
		$a = {60E9????????EF4003A7078F071C375D43A704B92C3A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
