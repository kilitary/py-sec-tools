rule _PE_Intro_v1_0_ekjclx
{
	meta:
		description = "PE Intro v1_0"
	strings:
		$a = {8A1602008A0732C2880743FEC281FB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
