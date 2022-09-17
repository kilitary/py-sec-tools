rule _Microsoft_Visual_C__v7_0_ejzrnm
{
	meta:
		description = "Microsoft Visual C__ v7_0"
	strings:
		$a = {6A0C6888BF0110E8B81C000033C0408945E48B750C33FF3BF7750C393D6C1E12100F84B3000000897DFC3BF0740583FE027531A1983612103BC7740CFF751056}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
