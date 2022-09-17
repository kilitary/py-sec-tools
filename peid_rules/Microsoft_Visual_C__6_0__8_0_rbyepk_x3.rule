rule _Microsoft_Visual_C__6_0__8_0_rbyepk
{
	meta:
		description = "Microsoft Visual C__ 6_0 _ 8_0"
	strings:
		$a = {68????????64A10000000050648925000000008B442410896C24108D6C24102BE05356578B45F88965E8508B45FCC745FCFFFFFFFF8945F8C38B4DF064890D00000000595F5E5BC951C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
