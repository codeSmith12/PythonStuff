extends CharacterBody2D


const SPEED = 150.0
const JUMP_VELOCITY = -250.0
var hasJumped = false
@onready var animated_sprite_2d: AnimatedSprite2D = $AnimatedSprite2D


func _physics_process(delta: float) -> void:
	# Add the gravity.
	if not is_on_floor():
		velocity += get_gravity() * delta
		animated_sprite_2d.play("jump")

	# Handle jump.
	if Input.is_action_just_pressed("jump") and is_on_floor():
		velocity.y = JUMP_VELOCITY
		hasJumped = true
		

	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
	var direction := Input.get_axis("moveLeft", "moveRight")
	
	
	
	
	if direction > 0:
		animated_sprite_2d.flip_h = false
	elif direction < 0:
		animated_sprite_2d.flip_h = true
	
	
	if is_on_floor():
		hasJumped = false
		if direction == 0:
			animated_sprite_2d.play("idle")
		elif direction > 0 or direction < 0:
			animated_sprite_2d.play("Run")
	else:
		if hasJumped == false:
			animated_sprite_2d.play("jump")
			hasJumped = true


	if direction:
		velocity.x = direction * SPEED
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
		

	move_and_slide()
