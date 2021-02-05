rule _Petite_v1_4_luwxql
{
	meta:
		description = "Petite v1_4"
	strings:
		$a = {B8????????669C60508BD8030068????????6A00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
