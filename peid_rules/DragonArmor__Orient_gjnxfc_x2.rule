rule _DragonArmor__Orient_gjnxfc
{
	meta:
		description = "DragonArmor __ Orient"
	strings:
		$a = {BF4C????0083C9FF33C06834????00F2AEF7D14951684C????00E8110A000083C40C684C????00FF1500????008BF0BF4C????0083C9FF33C0F2AEF7D149BF4C????008BD16834????00C1E902F3AB8BCA83E103F3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
