import { forwardRef, type HTMLAttributes, type ReactNode } from 'react'
import { cn } from '../../utils'

export interface AvatarProps extends HTMLAttributes<HTMLDivElement> {
  /** Avatar size */
  size?: 'sm' | 'md' | 'lg'
  /** Image source */
  src?: string
  /** Alt text for image */
  alt?: string
  /** Fallback initials or icon */
  children?: ReactNode
}

export const Avatar = forwardRef<HTMLDivElement, AvatarProps>(
  ({ size = 'md', src, alt, className, children, ...props }, ref) => {
    return (
      <div
        ref={ref}
        className={cn(
          'void-avatar',
          size !== 'md' && `void-avatar--${size}`,
          className,
        )}
        {...props}
      >
        {src ? <img src={src} alt={alt || ''} style={{ width: '100%', height: '100%', objectFit: 'cover' }} /> : children}
      </div>
    )
  }
)

Avatar.displayName = 'Avatar'

export interface AvatarGroupProps extends HTMLAttributes<HTMLDivElement> {
  children?: ReactNode
}

export const AvatarGroup = forwardRef<HTMLDivElement, AvatarGroupProps>(
  ({ className, children, ...props }, ref) => (
    <div ref={ref} className={cn('void-avatar-group', className)} {...props}>
      {children}
    </div>
  )
)

AvatarGroup.displayName = 'AvatarGroup'
