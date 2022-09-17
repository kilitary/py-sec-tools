rule _Vx_Phoenix_927_gglkpt
{
	meta:
		description = "Vx_ Phoenix_927"
	strings:
		$a = {E800005E81C6????BF0001B90400F3A4E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
