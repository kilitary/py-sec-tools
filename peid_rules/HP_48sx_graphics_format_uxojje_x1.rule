rule _HP_48sx_graphics_format_uxojje
{
	meta:
		description = "HP_48sx graphics format"
	strings:
		$a = {4850485034382D41}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
